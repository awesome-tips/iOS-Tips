聊聊 load 与 __attribute__ 
----------
**作者**: [Lefe_x](https://weibo.com/u/5953150140)

通常为了解耦或者其它目的，我们往往在 `+(void)load`方法做一些服务的启动或者利用运行时做方法的替换等。可以添加环境变量 `OBJC_PRINT_LOAD_METHODS=YES`打印 load 方法调用的顺序。如下：

```js
......

objc[159]: LOAD: +[_NSConstantNumberBool load]

objc[159]: LOAD: +[_NSConstantData load]

objc[159]: LOAD: +[_NSConstantDate load]

objc[159]: LOAD: +[_NSConstantDictionary load]

objc[159]: LOAD: class 'Annotation' scheduled for +load
objc[159]: LOAD: +[Annotation load]
```

load方法是在类被加入运行时中执行的，根据下面的源码即可知道`+(void)load`方法被调用的顺序：父类 > 类 > 分类1、分类2（分类之间的顺序是由编译顺序决定的）：

```c
void prepare_load_methods(const headerType *mhdr) {
    // 类的调用
    classref_t *classlist = 
        _getObjc2NonlazyClassList(mhdr, &count);
    for (i = 0; i < count; i++) {
        schedule_class_load(remapClass(classlist[i]));
    }
    // 分类的调用
    category_t **categorylist = _getObjc2NonlazyCategoryList(mhdr, &count);
    for (i = 0; i < count; i++) {
        category_t *cat = categorylist[i];
        add_category_to_loadable_list(cat);
    }
}

static void schedule_class_load(Class cls) {
    // 第一.调用父类的 +(void)load 方法
    schedule_class_load(cls->superclass);
    // 第二.调用类的 +(void)load 方法
    add_class_to_loadable_list(cls);
}

void add_class_to_loadable_list(Class cls) {
    if (PrintLoading) {
        // 类中Load 方法被调用后的打印，添加环境变量OBJC_PRINT_LOAD_METHODS即可看见这些打印信息
        _objc_inform("LOAD: class '%s' scheduled for +load", 
                     cls->nameForLogging());
    }
}

void add_category_to_loadable_list(Category cat) {
    // 分类类中Load 方法被调用后的打印，添加环境变量OBJC_PRINT_LOAD_METHODS即可看见这些打印信息
    if (PrintLoading) {
        _objc_inform("LOAD: category '%s(%s)' scheduled for +load", 
                     _category_getClassName(cat), _category_getName(cat));
    }
}
```

除了 load 方法之外，我们可以使用编译时的特性来做初始化的服务，比如下面的例子，下面这些方法会在main函数执行前调用，而且可以控制函数的执行顺序，对模块化用来解耦是一个不错的方案：

```c
// main 函数开始执行时调用
// 执行顺序为 before101，before102，before103
__attribute__((constructor(101)))
void before101() {
    NSLog(@"before101");
}

__attribute__((constructor(103)))
void before103() {
    NSLog(@"before103");
}

__attribute__((constructor(102)))
void before102() {
    NSLog(@"before102");
}
```


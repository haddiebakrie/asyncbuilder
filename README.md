AsyncBuilder
============

A class that builds an asynchronous widget and updates the UI based on the state of the task.

Attributes:
    :attr:`builder` :class:`ObjectProperty`: The asynchronous task to be executed.
    :attr:`value` :class:`StringProperty`: The result of the asynchronous task.
    :attr:`async_state` :class:`ObjectProperty`: The current state of the asynchronous task.
    :attr:`waiting` :class:`ObjectProperty`: The widget displayed while the task is running.
    :attr:`done` :class:`ObjectProperty`: The widget displayed with the result of the task once it is complete.

Both `waiting` and `done` can either be a `str` or a `function`.
If a `string` is passed, :meth:`kivy.factory.Factory.get` is called to 
obtain the Widget.
If a function is passed, the fuction must return a `Widget`.

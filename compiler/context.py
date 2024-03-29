class VariableInfo:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class FunctionInfo:
    def __init__(self, name, params):
        self.name = name
        self.params = params


class Scope:
    def __init__(self, parent=None):
        self.local_vars = []
        self.local_funcs = []
        self.parent = parent
        self.children = []
        self.var_index_at_parent = 0 if parent is None else len(
            parent.local_vars)
        self.func_index_at_parent = 0 if parent is None else len(
            parent.local_funcs)

    def create_child_scope(self):
        child_scope = Scope(self)
        self.children.append(child_scope)
        return child_scope

    def define_variable(self, vname, value, reassign=False):
        if reassign:
            if self.is_local_var(vname):
                self.get_local_variable_info(vname).value = value
                return
            elif self.parent is not None:
                self.parent.define_variable(vname, value, reassign)
                return
        else:
            self.local_vars.append(VariableInfo(vname, value))
            return

    def redefine_call_arg(self, vname, value):
        if self.is_local_var(vname):
            self.get_local_variable_info(vname).value = value

    def define_function(self, fname, params):
        if not self.is_func_defined(fname, len(params)):
            self.local_funcs.append(FunctionInfo(fname, params))
        return

    def is_var_defined(self, vname):
        for var in self.local_vars:
            if var.name == vname:
                return True
        for var in range(self.var_index_at_parent):
            if self.parent.local_vars[var].name == vname:
                return True
        return self.parent.is_var_defined(vname) if self.parent is not None else False

    def is_func_defined(self, fname, n):
        for func in self.local_funcs:
            if func.name == fname and len(func.params) == n:
                return True
        for func in range(self.func_index_at_parent):
            if self.parent.local_funcs[func].name == fname and len(self.parent.local_funcs[func].params) == n:
                return True
        return self.parent.is_func_defined(fname, n) if self.parent is not None else False

    def is_local_var(self, vname):
        return self.get_local_variable_info(vname) is not None

    def is_local_func(self, fname, n):
        return self.get_local_function_info(fname, n) is not None

    def get_local_variable_info(self, vname):
        for var in self.local_vars:
            if var.name == vname:
                return var
        return None

    def get_variable(self, vname):
        if self.is_local_var(vname):
            return self.get_local_variable_info(vname)
        elif self.parent is not None:
            return self.parent.get_variable(vname)
        else:
            return None

    def get_local_function_info(self, fname, n):
        for func in self.local_funcs:
            if func.name == fname and len(func.params) == n:
                return func
        return None

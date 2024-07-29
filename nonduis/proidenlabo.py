class Config:
    def __init__(self, **kwargs):
        self._initial_params = kwargs.copy()
        self._current_params = kwargs

    def set_param(self, key, value):
        self._current_params[key] = value

    def get_param(self, key):
        return self._current_params.get(key)

    def has_modified_params(self):
        """
        Tests if one or more parameters has been modified.
        If invoked with no parameters, it checks all parameters.
        """
        return self._initial_params != self._current_params

    def reset_to_initial(self):
        """Resets current parameters to their initial states."""
        self._current_params = self._initial_params.copy()

# Example usage
config = Config(param1="value1", param2="value2")
print("Initial state:", config._current_params)

# Modify a parameter
config.set_param("param1", "new_value1")
print("After modification:", config._current_params)

# Check if any parameter has been modified
if config.has_modified_params():
    print("One or more parameters have been modified.")
else:
    print("No parameters have been modified.")

# Reset to initial parameters
config.reset_to_initial()
print("After reset:", config._current_params)

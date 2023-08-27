PYTHON_DOCSTR_TEMPL = """
\"\"\"
<description of what the function does>
<any side effects caused by calling the function>

Args:
    <arg1>: <description of arg1>
    <arg2>: <description of arg2>
    ...

Returns:
    <description of what is returned by the function>

Raises:
    KeyError: <description of any exceptions that can be raised by the function.>
\"\"\"
d"""

CPP_DOCSTR_TEMPL = """
/**
 * <description of what the function does>
 *
 * This sum is the arithmetic sum, not some other kind of sum that only
 * mathematicians have heard of.
 *
 * @param values Container whose values are summed.
 * @return sum of `values`, or 0.0 if `values` is empty.
 */
"""
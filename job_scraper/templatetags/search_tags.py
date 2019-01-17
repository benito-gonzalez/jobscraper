from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Return encoded URL parameters that are the same as the current
    request's parameters, only with the specified GET parameters added or changed.
    It also removes any empty parameters to keep things neat,
    so you can remove a parm by setting it to ``""``.
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()


@register.simple_tag
def get_first_index(jobs_per_page, current_page):
    return jobs_per_page * (current_page - 1) + 1


@register.simple_tag
def get_last_index(jobs_per_page, current_page, total_jobs):
    if total_jobs < jobs_per_page * current_page:
        return total_jobs
    return jobs_per_page * current_page
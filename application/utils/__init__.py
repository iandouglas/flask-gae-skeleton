# coding=utf-8
import bleach


def sanitize_input(value):
    """
    strip content of XSS markings
    :param value: string value to sanitize
    """
    return bleach.linkify(bleach.clean(value))

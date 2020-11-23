from .core import parser as _parser, html_output, to_html, rules, rules_discord_only, rules_embed, md as markdown, \
    html_tag, classes, classes_discord_only, classes_embed


def parser(source):
    return _parser(source, {'inline': True})

from django import template
from TreeApp.models import MenuObject

register = template.Library()


def get_line_tree(line_to_get, given_lines_list):
    tree_list = []

    for line in given_lines_list:
        if line.line_parent == line_to_get or line == line_to_get or line == line_to_get.line_parent or line.line_parent == line_to_get.line_parent:

            tree_list.append(line)

    top_line_reached = False

    while not top_line_reached:
        for line in tree_list:
            if line.line_parent is not None and line.line_parent not in tree_list:
                tree_list.append(line.line_parent)

                for item in given_lines_list:
                    if line.line_parent == item.line_parent and item not in tree_list:

                        item_index = list(given_lines_list).index(item)
                        line_index = list(given_lines_list).index(line)

                        print(item_index, line_index)

                        if item_index < line_index:
                            tree_list.insert(0, item)
                        else:
                            tree_list.append(item)

            else:
                top_line_reached = True

    for line in given_lines_list:
        if line not in tree_list and line.line_parent is None:
            tree_list.append(line)

    return tree_list


def top_and_other_lines_lists(lines_list=[], previous_line=None):
    top_lines = []
    other_lines = []

    for line in lines_list:
        if previous_line is None:
            if line.line_parent is None or line.line_parent.id == line.id:
                top_lines.append(line)
            else:
                other_lines.append(line)
        else:
            if line.line_parent.id == previous_line.id and line.id != previous_line.id:
                top_lines.append(line)
            else:
                other_lines.append(line)
    
    return [top_lines, other_lines]


def find_parent_relations(lines_list=[], previous_line=None):

    if len(lines_list) > 0:
        get_lines_lists = top_and_other_lines_lists(lines_list=lines_list, previous_line=previous_line)

        top_lines = get_lines_lists[0]
        other_lines = get_lines_lists[1]
    else:
        top_lines = []

    result = []

    if len(top_lines) > 0:

        if len(other_lines) > 0:
            
            for line in top_lines:

                this_line_result_list = find_parent_relations(lines_list=other_lines, previous_line=line)

                if len(this_line_result_list) > 0 :
                    result.append([line, this_line_result_list])
                else:
                    result.append([line, None])
        else:
            for line in top_lines:
                result.append([line, None])

    return result


@register.inclusion_tag("menu.html", takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']

    menu_lines = MenuObject.objects.filter(menu_name__menu_name=menu_name)

    if request.path == "/":
        lines_list = find_parent_relations(lines_list=menu_lines)
    else:
        if len(menu_lines) > 0:
            requested_line = menu_lines.filter(line_name=context['line'])

            if len(requested_line) > 0:
                requested_line = requested_line[0]
            else:
                data = {"menu_name": "Item not found", "lines_list": [[None, None]]}
                return data

            lsit_for_given_line = get_line_tree(line_to_get=requested_line, given_lines_list=menu_lines)

            lines_list = find_parent_relations(lines_list=lsit_for_given_line)
        else:
            lines_list = [[None, None]]

    data = {"menu_name": menu_name, "lines_list": lines_list}
        
    return data

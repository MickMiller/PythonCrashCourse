""" Try It Yourself 9-13 """


def ordered_dict(local_dict):
    """ Code from pg 185 """
    local_dict['jen'] = 'python'
    local_dict['sarah'] = 'c'
    local_dict['edward'] = 'ruby'
    local_dict['phil'] = 'python'

    for name, language in local_dict.items():
        print(name.title() + "'s favorite language is: " +
              language.title())
        ret_val = language.title()

    return ret_val

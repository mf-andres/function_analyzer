import math


def get_domain_len(from_domain: int, to_domain: int, domain_step: int):
    domain_len = math.floor((to_domain - from_domain) / domain_step)
    return domain_len

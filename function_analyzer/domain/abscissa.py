from function_analyzer.domain.domain import get_domain_len


def get_abscissas(from_domain: int, to_domain: int, domain_step: int):
    abscissas = list()
    domain_len = get_domain_len(from_domain, to_domain, domain_step)
    abscissa = from_domain
    abscissas.append(abscissa)
    for _ in range(domain_len - 1):
        abscissa += domain_step
        abscissas.append(abscissa)
    return abscissas

import sys
from geocoder import get_coordinates, get_ll_span
from mapapi_PG import show_map


def main(toponim):
    ll, spn = get_ll_span(toponim)
    pt = ll + ',pmdom1'
    show_map(f'll={ll}&spn={spn}&pt={pt}')


if __name__ == '__main__':
    t = " ".join(sys.argv[1:])
    if t:
        main(t)
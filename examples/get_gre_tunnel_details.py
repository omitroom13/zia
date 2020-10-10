# -*- coding: utf-8 -*-

import zia


def main():

    print("\n\n ##########  STARTING SDK ##########\n\n")
    z = zia.zscaler()
    z.get_zia_partner_creds_from_env(True)
    z.set_cloud('betacloud')
    z.authenticate_partner_api()

    # Get all GRE tunnel details
    print("\n\n ##########  GET ALL GRE tunnel details ##########\n\n")
    z.get_gre_tunnel_details()


if __name__ == '__main__':
    main()

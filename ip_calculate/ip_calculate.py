#   2019-04-29 15:30:00
#   网络和 IP 地址计算



def ip_calculate():
    raw_data = input('输入网络地址。\t事例：23.123.324.123/28\n\n')
    ip, subnet_mask = raw_data.split('/')

    ip_list = ip.split('.')
    ip_list = [int(i) for i in ip_list]

    subnet_mask = int(subnet_mask)
    surplus_mask = 32 - subnet_mask

    subnet = '1' * subnet_mask + '0' *  surplus_mask
    subnet_list = [ int(subnet[:8], 2), int(subnet[8:16], 2), int(subnet[16:24], 2), int(subnet[24:], 2) ]

    ret_list = []
    for i in range(4):
        ret_list.append(ip_list[i] & subnet_list[0])

    print('可用网络地址总数：', 2 ** surplus_mask - 2)
    for i in range(2 ** surplus_mask):
        ret_ip_list = ret_list[::]
        ret_ip_list[-1] += i

        if not i:
            print( '网络地址： ', '.'.join([str(i) for i in ret_ip_list]) )
            print('可用 IP 地址：')
            continue

        if i + 1 == 2 ** surplus_mask:
            print( '广播地址： ', '.'.join([str(i) for i in ret_ip_list]) )
            continue

        print( '.'.join([str(i) for i in ret_ip_list]) )





if __name__ == '__main__':
    ip_calculate()
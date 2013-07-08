#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# This file is part of faketcp.
#
# faketcp is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# trooper-simulator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with faketcp. If not, see <http://www.gnu.org/licenses/>.

import argparse
import faketcp

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='FakeTCP client')

    parser.add_argument('host', metavar='HOST', type=str, help='hostname or ip address of the server')
    parser.add_argument('port', metavar='PORT', type=int, default=50007, nargs='?', help='port of the server')

    parser.add_argument('--ploss', metavar='PLOSS', type=float, default=0.0, help='probability of packet loss between 0.0 and 1.0, defaults to 0.0.')
    parser.add_argument('--pdup', metavar='PDUP', type=float, default=0.0, help='probability of packet duplication between 0.0 and 1.0, defaults to 0.0.')
    parser.add_argument('--pdelay', metavar='PDELAY', type=float, default=0.0, help='probability of packet delayed (and arriving out of order) between 0.0 and 1.0, defaults to 0.0.')

    parser.add_argument('-n', '--num', metavar='NUM', type=int, default=16, help='number of datagrams to send.')

    args = parser.parse_args()
    print args

    socket = faketcp.Socket(ploss=args.ploss, pdup=args.pdup, pdelay=args.pdelay)

    print 'Connecting to ', (args.host, args.port), '...'
    socket.connect((args.host, args.port))
    print 'Connection estabilished.'

    for i in range(args.num):
        socket.send('this is the packet number %d' % i)

    socket.close()
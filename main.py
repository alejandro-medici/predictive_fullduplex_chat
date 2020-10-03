# main entry point
from src.server import server
from src.client import client
import argparse


def main():
    """
    main entry point
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', metavar='int', type=int)
    parser.add_argument('--ip', metavar='string', type=str)
    parser.add_argument('--mode', metavar='string', type=str)
    
    args = parser.parse_args()
    if args.mode == 'server':
        _server = server(args.ip, args.port)
        _server.run()
    elif args.mode == 'client':
        _client = client(args.ip, args.port)
        _client.run()

if __name__ == "__main__":
    main()
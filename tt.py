#!/usr/bin/env python
from pydockertools.registry import registry_connect

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

#happy_bday.sing_me_a_song()
#
#bulls_on_parade.sing_me_a_song()
#
#foo = Song(happy_bday.lyrics)
#foo.sing_me_a_song()
#happy_bday.sing_me_a_song()
#
#

#parent_parser.add_argument("-p", type=int, required=True,
#                           help="set db parameter")
#help='types of A'


#parent_parser = argparse.ArgumentParser(add_help=False)
#parent_parser.add_argument('--parent', type=int)
#foo_parser = argparse.ArgumentParser(parents=[parent_parser])
#foo_parser.add_argument('foo')
#foo_parser.parse_args(['--parent', '2', 'XXX'])
#bar_parser = argparse.ArgumentParser(parents=[parent_parser])
#bar_parser.add_argument('--bar')
#bar_parser.parse_args(['--bar', 'YYY'])
#
#print bar_parser
#print foo_parser
import argparse, sys
class SubcommandHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def _format_action(self, action):
        parts = super(argparse.RawDescriptionHelpFormatter, self)._format_action(action)
        if action.nargs == argparse.PARSER:
            parts = "\n".join(parts.split("\n")[1:])
        return parts
    
parent_parser = argparse.ArgumentParser(conflict_handler='resolve', formatter_class=SubcommandHelpFormatter)
parent_parser._optionals.title = "OPTIONS"
parent_parser._positionals.title = "COMMANDS"
subparsers = parent_parser.add_subparsers(metavar=None, dest="subparser_name")

output_display = parent_parser.add_mutually_exclusive_group()
output_display.add_argument("-v", "--verbose", help="Increase output verbosity", action="count", default=False)
output_display.add_argument("-q", "--quiet", help="Suppress all output", action="store_true", default=False)

parser_registry = subparsers.add_parser("registry", #parents=[parent_parser],
                                      help="Registry related activities")
parser_registry.add_argument('-l', "--list-tags", help="Namespace for which tags should be listed", type=str, metavar='\b')
parser_registry.add_argument('-s', "--search", help="Search", type=str, metavar='\b')
parser_registry._optionals.title = "OPTIONS"
#parser_registry.set_defaults(commands='registry')
parser_swarm = subparsers.add_parser("swarm", 
                                      help="Swarm related operations")
parser_swarm._optionals.title = "OPTIONS"
#parser_swarm.set_defaults(commands='swarm')
if len(sys.argv)==1:
    parent_parser.print_help()
    sys.exit(1)
ARGS = vars(parent_parser.parse_args())
#print ARGS

if ARGS['subparser_name'] == 'registry':
    if ( ARGS.get('list_tags','e') or ARGS.get('search', 'e' )) == 'e':
        parser_registry.print_help()


#print ARGS


#
def registry(args):
    empty_keys  = [ k for k,v in args.iteritems() if v is None]
#    print empty_keys
    #for k in empty_keys:
    #    del args[k]
    #del args['subparser_name']
    #print args
    if args['list_tags']:
            if args['list_tags']:
                connection = registry_connect()
                for i in connection.list_tags(args['list_tags']):
                    pass
                sample = [i for i in connection.list_tags(args['list_tags'])]
                print sample
                str1 = ' '.join(sample)
                print str1
                print(max(map(len, str1.split())))
                #colsize = max(map(len, str1.split()))
                colsize = 10
                contents = ' '.join(('%*s' % (colsize, j) for j in str1.split()))
                print contents
                
    elif args['search']:
        print("search has been selected")

def search(args):
    print args
    if args['search']:
        connection = registry_connect()
        connection.search(search_name='debian')
    
#registry(ARGS)
search(ARGS)
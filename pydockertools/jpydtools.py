import argparse, sys
from .registry import registry_connect

# Thanks to Jeppe Ledet-Pedersen for this awesome class to remove the metavar
# http://stackoverflow.com/questions/13423540/argparse-subparser-hide-metavar-in-command-listing
class PositionalFormatter(argparse.RawDescriptionHelpFormatter):
    def _format_action(self, action):
        parts = super(argparse.RawDescriptionHelpFormatter, self)._format_action(action)
        if action.nargs == argparse.PARSER:
            parts = "\n".join(parts.split("\n")[1:])
        return parts

def parse_input():
    main_parser = argparse.ArgumentParser(
        description = "Jojees Python based Docker Tools for containers.",
        epilog='Note: arguments -u, -l are required when -c is missing.',
        conflict_handler='resolve',
        formatter_class=PositionalFormatter
    )
    main_parser._optionals.title = "General Options"
    main_parser._positionals.title = "Commands"
    subparsers = main_parser.add_subparsers(dest="subparser_name")
    output_display = main_parser.add_mutually_exclusive_group()
    output_display.add_argument("-v", "--verbose", help="Increase output verbosity", action="count", default=False)
    output_display.add_argument("-q", "--quiet", help="Suppress all output", action="store_true", default=False)
    main_parser.add_argument("--config", help="Use this config file", default=argparse.SUPPRESS, metavar='<config file>')
    
    parser_registry = subparsers.add_parser("registry", help="Registry related activities")
    parser_swarm = subparsers.add_parser("swarm", help="Swarm related operations")
    
    registry_options = parser_registry.add_mutually_exclusive_group()
    registry_options.add_argument("-l", "--list-tags", help="tags namespace. Ex: -l debian", type=str, metavar='')
    registry_options.add_argument("-s", "--search", help="Search for images. Ex: -s debian", type=str, metavar='')
    parser_registry._optionals.title = "OPTIONS"
    parser_swarm._optionals.title = "OPTIONS"
    if len(sys.argv)==1:
        main_parser.print_help()
        sys.exit(1)
    ARGS = vars(main_parser.parse_args())
    
    
    if ARGS['subparser_name'] == 'registry':
        if ( ARGS['list_tags'] or ARGS['search']) is None:
            print "entered list_tags"
            parser_registry.print_help()
            sys.exit(2)
    return ARGS

def registry_commands(args):
    if args['list_tags']:
        connection = registry_connect()
        for i in connection.list_tags(args['list_tags']):
            print i
    if args['search']:
        connection = registry_connect()
        for i in connection.search(search_name=args['search']):
            print i['name']
        
        
def swarm_commands(args):
    print 'Hey! This is swarm module'
    
subcommands_pool = {'registry':registry_commands, 'swarm': swarm_commands}

def main():
    parameters = parse_input()
    subcommands_pool[parameters['subparser_name']](parameters)    
    
if __name__ == "__main__":
    sys.exit(main())
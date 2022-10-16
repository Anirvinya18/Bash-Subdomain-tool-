import argparse
import re
import sys
# prevent creation of compiled bytecode files
sys.dont_write_bytecode = True
from recon.core import base
from recon.core.framework import Colors

def recon_ui(args):
    # set up command completion
    try:
        import readline
    except ImportError:
        print(f"{Colors.R}[!] Module 'readline' not available. Tab complete disabled.{Colors.N}")
    else:
        import rlcompleter
        if 'libedit' in readline.__doc__:
            readline.parse_and_bind('bind ^I rl_complete')
        else:
            readline.parse_and_bind('tab: complete')
        readline.set_completer_delims(re.sub('[/-]', '', readline.get_completer_delims()))
        # for possible future use to format command completion output
        #readline.set_completion_display_matches_hook(display_hook)
    # process toggle flag arguments
    flags = {
        'check': args.check if not args.stealth else False,
        'analytics': args.analytics if not args.stealth else False,
        'marketplace': args.marketplace if not args.stealth else False,
        'accessible' : args.accessible

#!/usr/bin/env python3
import olicybertools
import sys


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: \x1b[38;5;245mpython playerdiff.py\x1b[38;5;252m <\x1b[38;5;161muser1\x1b[38;5;252m> <\x1b[38;5;161muser2\x1b[38;5;252m> [\x1b[38;5;66m--title\x1b[38;5;252m|\x1b[38;5;66m--id\x1b[38;5;252m|\x1b[38;5;66m--both\x1b[38;5;252m] [--stats]")
        sys.exit(1)
    user1 = olicybertools.User(int(sys.argv[1]))
    user2 = olicybertools.User(int(sys.argv[2]))
    user1.get_stats()
    user2.get_stats()
    information = "id"
    if len(sys.argv) > 3:
        if sys.argv[3] in {"--title", "--id", "--both"}:
            information = sys.argv[3].removeprefix("--")
        if "--stats" in sys.argv:
            print()
            user1.print_basic_stats()
            user2.print_basic_stats()
    missing1 = user1.missing_challenges_from(user2, information)
    missing2 = user2.missing_challenges_from(user1, information)
    print(f"\n\x1b[31m{user2.nickname}\x1b[0m has solved \x1b[32m{len(missing1)}\x1b[0m challenges that \x1b[31m{user1.nickname}\x1b[0m has not solved")
    try:
        print('\n- ' + '\n- '.join([*missing1]))
    except TypeError:
        print('\n- ' + '\n- '.join([str(i) for i in missing1]))
    print(f"\n\x1b[31m{user1.nickname}\x1b[0m has solved \x1b[32m{len(missing2)}\x1b[0m challenges that \x1b[31m{user2.nickname}\x1b[0m has not solved")
    try:
        print('\n- ' + '\n- '.join([*missing2]))
    except TypeError:
        print('\n- ' + '\n- '.join([str(i) for i in missing2]))
#Created by robby parlan
#Modified by Abdullah

from optparse import OptionParser
import os.path
import re

class warna():
    cetak = '\033[0m'
    ijo ='\033[1;32m'
    putih = '\033[1;37m'
    biru = '\033[1;34m'
    kuning = '\033[1;33m'
    abang = '\033[1;31m'


regex = re.compile(r'''(
                   ([a-zA-Z0-9._%+-]+)
                    @
                    (gmail|yahoo|hotmail)
                    (\.com)
                    )''', re.VERBOSE)

def file_to_str(filename):
    with open(filename) as f:
        return f.read().lower()

def get_emails(s):
    return (email[0] for email in re.findall(regex, s) if not email[0].startswith('//'))

def main():
    parser = OptionParser()
    parser.add_option('-o','--output',dest='output',help='output file to saveFile.txt', action='store_true')
    (options, args) = parser.parse_args()
    try:
        if args and options.output:
            for arg in args:
                if os.path.isfile(arg):
                    for email in get_emails(file_to_str(arg)):
                        if 'gmail' in email:
                            f =open('gmailFile.txt', 'a')
                            f.write(email+'\n')
                            f.close()
                        elif 'yahoo' in email:
                            f = open('yahooFile.txt', 'a')
                            f.write(email + '\n')
                            f.close()
                        else:
                            f = open('hotmailFile.txt', 'a')
                            f.write(email + '\n')
                            f.close()
                    print("DONE!")
                    print('Succes filter to gmailFile.txt' % (warna.biru, warna.cetak))
                    print('Succes filter to yahooFile.txt' % (warna.kuning, warna.cetak))
                    print('Succes filter to hotmailFile.txt' % (warna.abang, warna.cetak))
                else:
                    print('"{}" is not a file.').format(arg)

        else:
            print("NOT DONE!")
    except Exception as e:
        print('Error Description', e)


if __name__=='__main__':
    main()

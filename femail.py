from verifyemail import verify_istrue
import argparse
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s')

logger = logging.getLogger()

def savefile(filename, data):
    with open(filename, 'a', encoding='utf-8')as f:
        f.write(data + '\n')

def main(emails, from_email ,outfile):
    try:
        result = verify_istrue(emails, from_email)
    except Exception as e:
        logger.error(e)
        return 
    for k,v in result.items():
        if v is True:
            savefile(outfile,k)
    logger.info('Task Finish!')

def readfile(filename):
    with open(filename,'r',encoding='utf-8')as f:
        datas = f.read()
    datas = datas.strip().split()
    return datas

if __name__ == '__main__':
    help = """by Scrboy.
单个email验证：
python femail.py -c xxx@abc.com
枚举邮箱模式：
python femail.py -b -d 163.com -f burpemails.txt
批量验证邮箱有效性模式：
python femail.py -v -f emails.txt"""
    # print(help)
    parser = argparse.ArgumentParser(usage=help)
    parser.add_argument('-c', '--check', type=str)
    parser.add_argument('-v', '--verify', action="store_true", default=False)
    parser.add_argument('-b', '--brute', action="store_true", default=False)
    parser.add_argument('-d', '--domain', type=str, default='qq.com')
    parser.add_argument('-f', '--file', type=str, default='emails.txt')
    parser.add_argument('-o', '--outfile', type=str, default='results.txt')
    args = parser.parse_args()
    if args.check:
        emails = [args.check]
    elif args.verify:
        emails = readfile(args.file)
    elif args.brute:
        emails = readfile(args.file)
        mailhost = '@' + args.domain
        emails = [email+mailhost for email in emails]
    else:
        logger.debug('input error')
    from_email = 'mbzcfy49358@chacuo.net'
    main(emails, from_email, args.outfile)

    
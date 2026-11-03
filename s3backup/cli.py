import argparse
import getpass
from s3backup.crypto import encrypt, decrypt
from s3backup.archive import make_archive, export_archive

parser = argparse.ArgumentParser(prog="s3backup", description="Encrypted backups to S3")
sub = parser.add_subparsers(dest="command", required=True)

backup = sub.add_parser("backup", help="encrypt a folder into backup file")
backup.add_argument("folder")
backup.add_argument("output")

restore = sub.add_parser("restore", help="decrypt a backup file into a folder")
restore.add_argument("input")
restore.add_argument("dest")

args = parser.parse_args()
passphrase = getpass.getpass("Passphrase: ")

if args.command == "backup":
    data = make_archive(args.folder)
    with open(args.output, "wb") as f:
        f.write(encrypt(data, passphrase))
    print("Backup written to", args.output)

elif args.command == "restore":
    with open(args.input, "rb") as f:
        data = decrypt(f.read(), passphrase)
    extract_archive(data, args.dest)
    print("Restored to", args.dest)

# -*- coding: utf-8 -*-

import argparse
import hashlib
import sys


def generate_hash(password, hashtype):
    try:
        hash_obj = getattr(hashlib, hashtype)()
        hash_obj.update(password.encode("utf-8"))
        return hash_obj.hexdigest()
    except AttributeError:
        return "Invalid hash type selected!"


def main():

    parser = argparse.ArgumentParser(description="Password Hash Generator")

    parser.add_argument(
        "password",
        nargs="?",
        help="Password to hash"
    )

    parser.add_argument(
        "-t", "--type",
        default="sha256",
        choices=["sha256", "sha512", "md5"]
    )

    args = parser.parse_args()

    # 👉 FIX: agar CLI se password nahi mila to user se input lo
    if not args.password:
        print("\nNo password provided via command line.")
        args.password = input("Enter password: ")

    result = generate_hash(args.password, args.type)

    print("\n==============================")
    print(" Hash Generator")
    print("==============================")
    print("Type   :", args.type)
    print("Input  :", args.password)
    print("Output :", result)
    print("==============================\n")


if __name__ == "__main__":
    main()
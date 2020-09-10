from datasette import hookimpl
import dns.resolver
import sqlite3

sqlite3.enable_callback_tracebacks(True)


def resolve_txt(hostname):
    return dns.resolver.resolve(hostname, "TXT").response


def dns_txt(hostname):
    try:
        message = resolve_txt(hostname)
    except dns.resolver.NoAnswer as e:
        return str(e)
    return message.to_text()


@hookimpl
def prepare_connection(conn):
    conn.create_function("dns_txt", 1, dns_txt)

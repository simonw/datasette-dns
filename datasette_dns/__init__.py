from datasette import hookimpl
import dns.resolver


def dns_txt(hostname):
    message = dns.resolver.resolve(hostname, "TXT").response
    return message.to_text()


@hookimpl
def prepare_connection(conn):
    conn.create_function("dns_txt", 1, dns_txt)

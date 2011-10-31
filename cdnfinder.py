import dns
import dns.message
import dns.query

CDN_PROVIDER  = [
    [".akamai.net", "Akamai"],
    [".akamaiedge.net", "Akamai"],
    [".llnwd.net", "Limelight"],
    ["edgecastcdn.net", "EdgeCast"],
    ["hwcdn.net", "Highwinds"],
    [".panthercdn.com", "Panther"],
    [".simplecdn.net", "Simple CDN"],
    [".instacontent.net", "Mirror Image"],
    [".footprint.net", "Level3"],
    [".ay1.b.yahoo.com", "Yahoo"],
    [".yimg.", "Yahoo"],
    [".google.", "Google"],
    ["googlesyndication.", "Google"],
    ["youtube.", "Google"],
    [".googleusercontent.com", "Google"],
    [".internapcdn.net", "Internap"],
    [".cloudfront.net", "Amazon Cloudfront"],
    [".netdna-cdn.com", "MaxCDN"],
    [".netdna-ssl.com", "MaxCDN"],
    [".netdna.com", "MaxCDN"],
    [".cotcdn.net", "Cotendo"],
    [".cachefly.net", "Cachefly"],
    ["bo.lt", "BO.LT"],
    [".cloudflare.com", "Cloudflare"],
    [".afxcdn.net", "afxcdn.net"],
    [".lxdns.com", "lxdns.com"],
    [".att-dsa.net", "AT&T"],
    [".vo.msecnd.net", "Windows Azure"],
    [".voxcdn.net", "Voxel"],
    [".bluehatnetwork.com", "Blue Hat Network"],
    [".swiftcdn1.com", "SwiftCDN"],
    [".rncdn1.com", "Reflected Networks"],
    [".cdngc.net", "CDNetworks"],
    [".fastly.net", "Fastly"],
    [".gslb.taobao.com", "Taobao"],
    [".gslb.tbcache.com", "Alimama"]
]

def finder(host):
    result = None
    for cdn in CDN_PROVIDER:
        if cdn[0] in host:
            return cdn[1]
    return None

def findcdnfromhost(host, dnsip = "8.8.8.8"):
    newhost = host
    try:
        q = dns.message.make_query(host, "A")
        r = dns.query.udp(q, dnsip)
        for ans in r.answer:
            if "CNAME" in ans.to_text():
                newhost = ans.to_text().split("CNAME ")[1][:-1]
    except:
        return finder(newhost)
    return finder(newhost)

if __name__ == "__main__":
    import sys
    print findcdnfromhost(sys.argv[-1])

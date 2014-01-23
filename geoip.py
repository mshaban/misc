import pygeoip


# Load the database once and store it globally in interpreter memory.


if __name__ == '__main__':
	gi = pygeoip.GeoIP('/Users/mohamed/Downloads/GeoIP.dat')
	gi4.country_code_by_name('google.com')
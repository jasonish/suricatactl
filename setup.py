from setuptools import setup

version = "0.0.1"

# def write_revision():
#     try:
#         revision = subprocess.check_output(
#             ["git", "rev-parse", "--short", "HEAD"])
#         with open("./suricata/update/revision.py", "w") as fileobj:
#             fileobj.write("revision = '%s'" % (revision.strip()))
#     except Exception as err:
#         print("Failed to get current git revision: %s" % (err))

# write_revision()

setup(
    name="suricatactl",
    version=version,
    description="Suricata Control Tool",
    author="Jason Ish",
    author_email="ish@unx.ca",
    packages=[
        "suricata",
        "suricata.ctl",
    ],
    url="https://github.com/jasonish/suricatactl",
    license="GPLv2",
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ],
    scripts = [
        "bin/suricatactl",
    ],
)

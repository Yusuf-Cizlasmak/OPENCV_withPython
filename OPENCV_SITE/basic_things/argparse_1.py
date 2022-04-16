#argparse artık bizim için önemli olacak çünkü kodu falan çağırırken artık dosya yolunu veya kodu cmd çalıştırırken işimize yarıyacak.

#bu gerekli bir paket artık bizim için.
import argparse
# construct the argument parse and parse the arguments
ap=argparse.ArgumentParser() #ArgumentParser zaten anlamı argument bölüştürücü demek oradan çak köfteyi
ap.add_argument("--name",required=True,help="name of the user")
args=vars(ap.parse_args())

#bakalım ne işe yarayacakmış?
print("Merhaba {},seninle tanıştığıma sevindim".format(args["name"]))


#terminalden çalıştırırken ilk önce python sonra adı sonra --name (yani key ) en son value olacak şekilde ilerleyeceksin oki doki.

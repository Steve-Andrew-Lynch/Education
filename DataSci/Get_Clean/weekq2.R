setwd("Education/DataSci/Get_Clean")

library("httpuv")
library("httr")
library("jsonlite")

oauth_endpoints("github")

myapp <- oauth_app("github", "15e3788418949c46803f", "25332c5c2785e6e3b9517bf0d8d4b5813393999e")

github_token <- oauth2.0_token(oauth_endpoints("github"), myapp)
req <- GET("https://api.github.com/users/jtleek/repos", config(token = github_token))
stop_for_status(req)
content(req)

jsonData <- fromJSON("https://api.github.com/users/jtleek/repos")
json1 = jsonlite::fromJSON("https://api.github.com/users/jtleek/repos")
names(json1)
json1[json1[,2]=="datasharing",45]

library("sqldf")
csvURL <- "https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06pid.csv"
download.file(csvURL, destfile = "acs.csv", method="curl")
acs <- read.csv("acs.csv")
head(acs)
sqldf("select pwgtp1 from acs where AGEP < 50")
sqldf("select distinct AGEP from acs")

nchar(readLines("http://biostat.jhsph.edu/~jleek/contact.html"))[c(10, 20, 30, 100)]

forURL <- "https://d396qusza40orc.cloudfront.net/getdata%2Fwksst8110.for"
download.file(forURL, destfile = "dat1.for", method="curl")
myfwf <- read.fwf("dat1.for", skip=4, widths = c(12,7,4,9,4,9,4,9,4), n=1254)
sum(myfwf[,4])
setwd("Education/DataSci/Get_Clean")
library("stringr")

acs <- read.csv("acs1.csv")
download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv", destfile = "acs1.csv", method = "curl")
acs_n_list <- strsplit(names(acs), "wgtp")
acs_n_list[[123]]

download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FGDP.csv", destfile = "gdp_dat.csv", method = "curl")
gdp_dat <- read.csv("gdp_dat.csv", na.strings = "", stringsAsFactors=F)
download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FEDSTATS_Country.csv", destfile = "edu_dat.csv", method = "curl")
edu_dat <- read.csv("edu_dat.csv", na.strings = "", stringsAsFactors=F)
gdp_dat <-gdp_dat[c(5:219),]
# names(gdp_dat)
# names(edu_dat)

gdp_dat_avg <- gdp_dat[c(1:190),]
gdp_dat_avg$"X.3" <-str_trim(gdp_dat_avg$"X.3")
gdp_dat_avg$"X.3" <-gsub(",", "", gdp_dat_avg$"X.3")
gdp_dat_avg$"X.3" <- as.numeric(gdp_dat_avg$"X.3")
mean(gdp_dat_avg$"X.3")

length(grep("^United", gdp_dat_avg$"X.2"))

merged_dat <- merge(edu_dat, gdp_dat, all = F, by.x ="CountryCode", by.y="X")
# merged_dat[0, 10] 
grep("*June*", merged_dat[,10])
june_dates <- merged_dat[grep("*Fiscal year end: June 30*", merged_dat[,10]),]
length(june_dates[,1])


install.packages("quantmod", dependencies = TRUE)
library("quantmod")
amzn = getSymbols("AMZN",auto.assign=FALSE)
sampleTimes = index(amzn)
sampleTimes <- format(sampleTimes, "%A, %y")
ind_2012 <- grep("(.*)2", sampleTimes)
sample_2012 <- sampleTimes[ind_2012]
length(sample_2012)
sample_Mondays <- grep("^Monday", sample_2012)
length(sample_Mondays)




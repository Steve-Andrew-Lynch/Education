setwd("Education/DataSci/Get_Clean") 
download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv", destfile = "acs1.csv", method = "curl")
acs <- read.csv("acs1.csv")

agricultureLogical <- acs$AGS == 6 & acs$ACR == 3
head(which(agricultureLogical), n=3)

install.packages("jpeg")
library("jpeg")
download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fjeff.jpg", destfile = "jeff.jpeg", method = "curl", mode = "wb")
image <- readJPEG("jeff.jpeg", TRUE)
quantile(image, probs = c(.3,.8))


download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FGDP.csv", destfile = "gdp_dat.csv", method = "curl")
gdp_dat <- read.csv("gdp_dat.csv", na.strings = "", stringsAsFactors=F)
download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FEDSTATS_Country.csv", destfile = "edu_dat.csv", method = "curl")
edu_dat <- read.csv("edu_dat.csv", na.strings = "", stringsAsFactors=F)
gdp_dat <-gdp_dat[c(5:219),]
names(gdp_dat)
names(edu_dat)
merged_dat <- merge(edu_dat, gdp_dat, all = F, by.x ="CountryCode", by.y="X")
merged_dat$"Gross.domestic.product.2012" <- as.numeric(merged_dat$"Gross.domestic.product.2012")
merged_dat <- merged_dat[merged_dat$"Gross.domestic.product.2012" > 0,]

ordered_dat <- merged_dat[order(merged_dat$"Gross.domestic.product.2012", decreasing=T),]
ordered_dat <- ordered_dat[complete.cases(ordered_dat$"X.2"), ]
ordered_dat[13,]
dim(ordered_dat)
names(ordered_dat)

head(ordered_dat)
unique(ordered_dat$Income.Group)
mean(ordered_dat$"Gross.domestic.product.2012"[ordered_dat$Income.Group == "High income: OECD"])
mean(ordered_dat$"Gross.domestic.product.2012"[ordered_dat$Income.Group == "High income: nonOECD"])

ordered_dat$"Gross.domestic.product.2012" <- sapply(ordered_dat$"Gross.domestic.product.2012", as.numeric)
ordered_dat$"Quantiles" <- cut(ordered_dat$"Gross.domestic.product.2012", breaks = quantile(ordered_dat$"Gross.domestic.product.2012", probs = seq(0, 1, 0.2)), include.lowest = TRUE, labels = 1:5)
table(ordered_dat$"Quantiles", ordered_dat$"Income.Group")

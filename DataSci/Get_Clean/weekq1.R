setwd("Education/DataSci/Get_Clean") 
download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv", destfile = "acs1.csv", method = "curl")
acs <- read.csv("acs1.csv")
sum(acs$VAL == 24, na.rm=T)

library("xlsx")
download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FDATA.gov_NGAP.xlsx", "gas_data.xlsx", method = "curl")
dat <- read.xlsx("gas_data.xlsx", sheetIndex = 1, rowIndex = 18:23, colIndex = 7:15)
sum(dat$Zip*dat$Ext, na.rm=T)

library("XML")
download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Frestaurants.xml", "rest_dat.xml", method = "curl")
doc <- xmlTreeParse("rest_dat.xml", useInternalNodes = T)
rootNode=xmlRoot(doc)
rootNode[[1]][[1]]
xmlChildren(rootNode[[1]][[1]])
sum(xpathSApply(doc,"//zipcode",xmlValue) == 21231)

library("data.table")
download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06pid.csv", "acs_data2.csv", method = "curl")
DT <- fread("acs_data2.csv")
system.time(DT[,mean(pwgtp15),by=SEX])


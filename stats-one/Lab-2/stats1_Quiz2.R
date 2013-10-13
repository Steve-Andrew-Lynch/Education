hw <- read.table("Stats1.13.HW.02.txt", header = T)
names(hw)
dim(hw)

mean(hw$SR)

aSR <- hw$SR
var(aSR)
pretest <- subset(hw, hw[,3]=="pre")
pretest

posttest <- subset(hw, hw[,3]=="post")
posttest

mean(pretest$SR)

mean(posttest$SR)

median(posttest$SR)

max(posttest$SR)

sd(posttest$SR)

describeBy(posttest, posttest$SR) 



WMp <- subset(hw, hw[,2]=="WM" & hw[, 3]=="pre")
WMt <- subset(hw, hw[,2]=="WM" & hw[, 3]=="post")
PEp <- subset(hw, hw[,2]=="PE" & hw[, 3]=="pre")
PEt <- subset(hw, hw[,2]=="PE" & hw[, 3]=="post")
DSp <- subset(hw, hw[,2]=="DS" & hw[, 3]=="pre")
DSt <- subset(hw, hw[,2]=="DS" & hw[, 3]=="post")

par(mfrow = c(2,3))
hist(DSp[, 4])
hist(DSt[, 4])
hist(WMp[, 4])
hist(WMt[, 4])
hist(PEp[, 4])
hist(PEt[, 4])
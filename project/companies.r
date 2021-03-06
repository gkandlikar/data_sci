library('RSQLite')
library('ggplot2')
setwd("~/Desktop/github/data_sci/project")
sqlite <- dbDriver("SQLite")
companiesdb <- dbConnect(sqlite,"companies.db")
dbListTables(companiesdb)
dbListFields(companiesdb,"companies")
results<-dbGetQuery(companiesdb,"SELECT name, categorycode from companies where categorycode is not null")
c <- ggplot(results, aes(categorycode))
c + geom_bar()
cat_freq<-as.data.frame(table(results$categorycode))
colnames(cat_freq) <- c("Category", "Count")
d <- ggplot(cat_freq, aes(x=Category, y=Count, fill=factor(Category)))
d <- d + theme(legend.position='none', axis.text.x=element_text(angle=90))
e <- d + geom_bar()
e
e+coord_polar()
pie(cat_freq$Count, labels=cat_freq$Category, main='Pie Chart')
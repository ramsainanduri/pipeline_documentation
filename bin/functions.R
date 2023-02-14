camel <- function(x){ #function for camel case
    capit <- function(x) paste0(toupper(substring(x, 1, 1)), substring(x, 2, nchar(x)))
    sapply(strsplit(as.character(x), "\\."), function(x) paste(capit(x), collapse=""))
}


round_df <- function(df, digits) {
  nums <- vapply(df, is.numeric, FUN.VALUE = logical(1))

  df[,nums] <- round(df[,nums], digits = digits)

  return(df)
}

highlight_text <- function(x, color,weight="normal",type="normal") {
  sprintf("<span style='color: %s;font-weight: %s;font-style: %s;'>%s</span>", color,weight,type,x)
}

get_unique_keys <- function(data) {#function to get unique keys from the data in yaml dict
    unique_keys <- unique(gsub("\\..*","",colnames(as.data.frame(data))))
    return(unique_keys)
}


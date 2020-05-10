#!/bin/bash

echo -n "This is question say (y/n)? "
read ans

if ["$ans" == "${ans#[Yy]}"];
then
  echo "Ans is yes"
else 
  echo "Ans is no"
fi

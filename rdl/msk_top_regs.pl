#! /usr/bin/perl

open(FILE, "msk_top_regs.rdl"); 

while(<FILE>) {

   	chomp;

   	s/}; \/\/ //;

   	$line = "$_\n";

   	if (/^\/\/.*desyrdl/) {
   			$line = substr $line, 2;
   	}

   	if (/name/) { $line = ""; }

   	if (/desc/) { 
   			$line = "";
   			$eoc = 1;
   	}

   	if (/;$/) {
   		if ($eoc == 1) {
   			$eoc = 0;
   			$line = "";
   		}
   	}

   	if (/Pluto_MSK_Modem/) { last; }

	print($line);

}
close FILE;

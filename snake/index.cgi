#!/usr/local/bin/perl
use CGI;
use HTML::Template;

my $template = HTML::Template->new(filename=>'web.html'); 
print"Content-type:text/html\n\n", $template->output; 


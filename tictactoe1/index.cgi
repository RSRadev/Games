#!/usr/local/bin/perl
use CGI;
use HTML::Template::Pro;

my($i, @board);

my $template = HTML::Template::Pro->new(
	filename=>'tictactoe.html',
	case_sensiteve=>1);

my $cgi = new CGI;
for($i=0; $i<9; $i++){
$template->param("BOARD$i"=>$board[$i]);
}
print"Content-type:text/html\n\n";

$template->output(print_to=>\*STDOUT);

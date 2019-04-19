#!/usr/local/bin/perl
use HTML::Template::Pro;
use CGI;
use strict;
use warnings;

my $template = HTML::Template::Pro->new(
	filename=>'index.html',
	case_sensitive=>1); 

my $cgi = new CGI;

my (@board,$blank, $i, $winner);
$winner;
print "Content-type:text/html\n\n";

if($cgi->param('sq0') or $cgi->param('sq1') or $cgi->param('sq2') or $cgi->param('sq3') or $cgi->param('sq4') or $cgi->param('sq5') or $cgi->param('sq6') or $cgi->param('sq7') or $cgi->param('sq8')){ 

for($i=0; $i<9; $i++ ){
$board[$i] = $cgi->param("sq$i");
$template->param("BOARD$i"=>$board[$i]);
 }
 if(($board[0] eq "x" && $board[1] eq "x" && $board[2] eq "x") || ($board[3] eq "x" && $board[4] eq "x" && $board[5] eq "x") || ($board[6] eq "x" && $board[7] eq "x" && $board[8] eq "x")
 || ($board[0] eq "x" && $board[3] eq "x" && $board[6] eq "x") || ($board[1] eq "x" && $board[4] eq "x" && $board[7] eq "x") || ($board[2] eq "x" && $board[5] eq "x" && $board[8] eq "x") || 
($board[0] eq "x" && $board[4] eq "x" && $board[8] eq "x") || ($board[2] eq "x" && $board[4] eq "x" && $board[6] eq "x")){
 	$winner="x";
       	print "X wins!"	
 }	
 for($i=0; $i<9; $i++){
	unless($board[$i]){
		 $blank = 1;
		}			
	}
	if($blank==1 && $winner eq undef){
	$i=int(rand(8)); 
	while($board[$i]){
		$i = int(rand(8));
	}
	$board[$i] = 'o';
	if(($board[0] eq "o" && $board[1] eq "o" && $board[2] eq "o") || ($board[3] eq "o" && $board[4] eq "o" && $board[5] eq "o") || ($board[6] eq "o" && $board[7] eq "o" && $board[8] eq "o")
 || ($board[0] eq "o" && $board[3] eq "o" && $board[6] eq "o") || ($board[1] eq "o" && $board[4] eq "o" && $board[7] eq "o") || ($board[2] eq "o" && $board[5] eq "o" && $board[8] eq "o") ||
($board[0] eq "o" && $board[4] eq "o" && $board[8] eq "o") || ($board[2] eq "o" && $board[4] eq "o" && $board[6] eq "o")){
 	$winner="o";
       print "O wins!";	
 }	
}elsif($blank==0 && $winner eq undef){
 	$winner = "d";
 	print "Draw!"; 


		
}	
	$template->param("WINNER"=>$winner);
	$template->param("BOARD$i"=>$board[$i]);
}
$template->output(print_to=>\*STDOUT);

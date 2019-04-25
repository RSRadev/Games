#!/usr/local/bin/perl -wT
use strict;
use HTML::Template::Pro;
use CGI;

my $template = HTML::Template::Pro->new(
	filename=>'index.html'
);
my $cgi=new CGI;

my $rabbit = "rabbit.jpg" ; 
my $gun    = "gun.jpg" ;
my $carrot = "carrot.jpg" ;

my @items =($rabbit, $gun, $carrot);

print"Content-type:text/html\n\n";

my $choose_rabbit  = $cgi->param('rabbit') 	|| undef;
my $choose_gun     = $cgi->param('gun') 	|| undef;
my $choose_carrot  = $cgi->param('carrot') 	|| undef;

srand();

if($choose_rabbit eq 'rab' or $choose_gun eq 'gu' or $choose_carrot eq 'car'){
	
	my $computer  = $items[rand @items]; 
	
	if($choose_rabbit eq 'rab' && $computer eq $items[1] ){
		$template->param(PLAYER=>$rabbit);
		$template->param(COMPUTER=>$gun);
		$template->param(WINNER=>$gun); 
		$template->param(WINNER_TEXT=> "GUN" ); 
	}elsif( $choose_gun  eq 'gu' && $computer eq $items[2]){
		$template->param(PLAYER=>$gun);
		$template->param(COMPUTER=>$carrot);
		$template->param(WINNER=>$carrot); 
		$template->param(WINNER_TEXT=> "CARROT" ); 
	}elsif( $choose_carrot  eq 'car' && $computer eq $items[0]){
		$template->param(PLAYER=>$carrot);
		$template->param(COMPUTER=>$rabbit);
		$template->param(WINNER=>$rabbit); 	
		$template->param(WINNER_TEXT=> "RABBIT" ); 
	}elsif( $choose_carrot eq 'car' && $computer eq $items[1]){
		$template->param(PLAYER=>$carrot);
		$template->param(COMPUTER=>$gun);
		$template->param(WINNER=>$carrot);
		$template->param(WINNER_TEXT=> "CARROT" ); 
	}elsif( $choose_rabbit eq 'rab' && $computer eq $items[2]){
		$template->param(PLAYER=>$rabbit);
		$template->param(COMPUTER=>$carrot);
		$template->param(WINNER=>$rabbit); 
		$template->param(WINNER_TEXT=> "RABBIT" ); 
	}elsif( $choose_gun eq 'gu' && $computer eq $items[0]){
		$template->param(PLAYER=>$gun);
		$template->param(COMPUTER=>$rabbit);
		$template->param(WINNER=>$gun); 
		$template->param(WINNER_TEXT=> "GUN" ); 
	}else{	
		$template->param(PLAYER=>$computer);
		$template->param(COMPUTER=>$computer);
		$template->param(WINNER_TEXT=> "DRAW" ); 
		$template->param(WINNER=>$computer);
	}
}
$template->output; 


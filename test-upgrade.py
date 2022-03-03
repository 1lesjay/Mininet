from mininet.topo import Topo



class MyTopo( Topo ):



	def __init__( self ):

	

		Topo.__init__( self )

		

		leftHost1 = self.addHost( 'h1' )
		leftHost2 = self.addHost( 'h2' ) 
		leftHost3 = self.addHost( 'h3’ )
		leftHost4 = self.addHost( 'h4’ )		          
		rightHost1 = self.addHost( 'h5’ )
		rightHost2 = self.addHost( 'h6’ )
		rightHost3 = self.addHost( 'h7’ )
		rightHost4 = self.addHost( 'h8’ )
		leftSwitch1 = self.addSwitch( 's1' )
        leftSwitch2 = self.addSwitch( 's2’ )
        leftSwitch3 = self.addSwitch( 's3’ )
        leftSwitch4 = self.addSwitch( 's4’ )
        leftSwitch5 = self.addSwitch( 's5’ )
		rightSwitch1 = self.addSwitch( 's6’ ) 
		rightSwitch2 = self.addSwitch( 's7’ ) 
		rightSwitch3 = self.addSwitch( 's8’ ) 
		rightSwitch4 = self.addSwitch( 's9’ ) 
		rightSwitch5 = self.addSwitch( 's10’ ) 


		self.addLink( leftHost1, leftSwitch1 )
		self.addLink( leftHost2, leftSwitch1 )
		self.addLink( leftHost3, leftSwitch2 )
		self.addLink( leftHost4, leftSwitch2 )
		self.addLink( rightHost5, rightSwitch1 )
		self.addLink( rightHost6, rightSwitch1 )
		self.addLink( rightHost7, rightSwitch2 )
		self.addLink( rightHost8, rightSwitch2 )
		self.addLink( leftSwitch1, leftSwitch3 )
        self.addLink( leftSwitch1, leftSwitch4 )
		self.addLink( leftSwitch2, leftSwitch3 )
		self.addLink( leftSwitch2, leftSwitch4 )
		self.addLink( rightSwitch1, rightSwitch3 )
		self.addLink( rightSwitch1, rightSwitch4 )
        self.addLink( rightSwitch2, rightSwitch3 )
		self.addLink( rightSwitch2, rightSwitch4 )
        self.addLink( leftSwitch3, leftSwitch5 )
		self.addLink( leftSwitch4, rightSwitch5 )
        self.addLink( rightSwitch3, leftSwitch5 )
		self.addLink( rightSwitch4, rightSwitch5 )

topos = { 'mytopo': ( lambda: MyTopo() ) }

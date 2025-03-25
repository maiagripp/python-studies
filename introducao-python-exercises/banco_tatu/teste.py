import unittest
from banco_Tatu.cliente import Cliente

class TestCliente(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.cliente1 = Cliente("João Silva", "12345-6")
        self.cliente2 = Cliente("Maria Souza", "98765-4")
    
    def test_cliente_creation(self):
        """Test that clients are created correctly with proper attributes."""
        self.assertEqual(self.cliente1.nome, "João Silva")
        self.assertEqual(self.cliente1.conta, "12345-6")
        self.assertEqual(self.cliente2.nome, "Maria Souza")
        self.assertEqual(self.cliente2.conta, "98765-4")
    
    def test_cliente_uniqueness(self):
        """Test that different clients are unique objects."""
        self.assertIsNot(self.cliente1, self.cliente2)
        self.assertNotEqual(self.cliente1.nome, self.cliente2.nome)
        self.assertNotEqual(self.cliente1.conta, self.cliente2.conta)
    
    def test_depositar(self):
        """Test deposit functionality."""
        initial_saldo = self.cliente1.saldo
        self.cliente1.depositar(100)
        self.assertEqual(self.cliente1.saldo, initial_saldo + 100)
    
    def test_sacar(self):
        """Test withdrawal functionality."""
        self.cliente1.depositar(200)  # Ensure sufficient funds
        initial_saldo = self.cliente1.saldo
        self.cliente1.sacar(50)
        self.assertEqual(self.cliente1.saldo, initial_saldo - 50)
    
    def test_sacar_insufficient_funds(self):
        """Test withdrawal with insufficient funds."""
        initial_saldo = self.cliente1.saldo
        large_amount = initial_saldo + 1000
        with self.assertRaises(ValueError):
            self.cliente1.sacar(large_amount)
        # Balance should remain unchanged
        self.assertEqual(self.cliente1.saldo, initial_saldo)
    
    def test_transferir(self):
        """Test transfer between accounts."""
        self.cliente1.depositar(500)
        cliente1_initial = self.cliente1.saldo
        cliente2_initial = self.cliente2.saldo
        
        transfer_amount = 200
        self.cliente1.transferir(self.cliente2, transfer_amount)
        
        self.assertEqual(self.cliente1.saldo, cliente1_initial - transfer_amount)
        self.assertEqual(self.cliente2.saldo, cliente2_initial + transfer_amount)

if __name__ == "__main__":
    unittest.main()
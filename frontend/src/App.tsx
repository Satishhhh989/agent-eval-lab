import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import { Activity, LayoutDashboard, Settings, BrainCircuit } from 'lucide-react';

const queryClient = new QueryClient();

const Sidebar = () => (
  <div className="w-64 glass h-full fixed left-0 top-0 flex flex-col p-4 border-r border-white/10 z-10">
    <div className="flex items-center gap-3 mb-8 px-2">
      <BrainCircuit className="w-8 h-8 text-primary" />
      <span className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-primary to-secondary">AgentEval</span>
    </div>

    <nav className="flex flex-col gap-2">
      <Link to="/" className="flex items-center gap-3 px-4 py-3 rounded-xl hover:bg-white/5 transition-colors">
        <LayoutDashboard className="w-5 h-5 text-gray-400" />
        <span className="font-medium text-gray-200">Dashboard</span>
      </Link>
      <Link to="/experiments" className="flex items-center gap-3 px-4 py-3 rounded-xl hover:bg-white/5 transition-colors">
        <Activity className="w-5 h-5 text-gray-400" />
        <span className="font-medium text-gray-200">Experiments</span>
      </Link>
      <Link to="/settings" className="flex items-center gap-3 px-4 py-3 rounded-xl hover:bg-white/5 transition-colors">
        <Settings className="w-5 h-5 text-gray-400" />
        <span className="font-medium text-gray-200">Settings</span>
      </Link>
    </nav>
  </div>
);

const Dashboard = () => (
  <div className="animate-fade-in relative z-0">
    {/* Decorative background glow */}
    <div className="absolute top-[-20%] left-[-10%] w-[500px] h-[500px] bg-primary/20 blur-[120px] rounded-full pointer-events-none" />
    <div className="absolute bottom-[-20%] right-[-10%] w-[600px] h-[600px] bg-secondary/10 blur-[150px] rounded-full pointer-events-none" />

    <header className="mb-8 relative z-10">
      <h1 className="text-3xl font-bold text-white mb-2">Agent Evaluation Laboratory</h1>
      <p className="text-gray-400">Monitor and scientifically compare autonomous AI agents.</p>
    </header>

    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8 relative z-10">
      {[
        { title: 'Reasoning Score', value: '94.2%' },
        { title: 'Tool Execution Rate', value: '88.5%' },
        { title: 'Cost per Run', value: '$0.42' }
      ].map((metric, i) => (
        <div key={i} className="glass-card p-6 animate-slide-up" style={{animationDelay: `${i * 100}ms`}}>
          <h3 className="text-lg font-medium text-gray-400 mb-2">{metric.title}</h3>
          <p className="text-3xl font-bold text-white">{metric.value}</p>
        </div>
      ))}
    </div>

    <div className="glass-card p-6 min-h-[400px] relative z-10">
      <h3 className="text-xl font-semibold text-white mb-4">Live Benchmark Results</h3>
      <div className="flex items-center justify-center h-64 border border-dashed border-white/20 rounded-xl">
        <p className="text-gray-500">Recharts Visualization Space</p>
      </div>
    </div>
  </div>
);

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <div className="flex min-h-screen">
          <Sidebar />
          <main className="flex-1 ml-64 p-8">
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/experiments" element={<div className="text-white animate-fade-in">Experiments View</div>} />
              <Route path="/settings" element={<div className="text-white animate-fade-in">Settings View</div>} />
            </Routes>
          </main>
        </div>
      </BrowserRouter>
    </QueryClientProvider>
  );
}

export default App;

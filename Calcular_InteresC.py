<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>La Segunda Guerra Mundial: El Gran Desmadre</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        /* Custom Chart Container Styling per Requirements */
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 600px; /* Constraint to prevent excessive width */
            margin-left: auto;
            margin-right: auto;
            height: 300px; /* Base height */
            max-height: 400px;
        }
        
        @media (min-width: 768px) {
            .chart-container {
                height: 350px; /* Taller on desktop */
            }
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        ::-webkit-scrollbar-thumb {
            background: #D32F2F;
            border-radius: 5px;
        }

        /* Material Design Card Hover Effect */
        .hover-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.12), 0 4px 8px rgba(0,0,0,0.06);
            transition: all 0.3s cubic-bezier(.25,.8,.25,1);
        }
    </style>
    <!-- 
    CHOSEN PALETTE: VIBRANT / ENERGETIC
    Red: #D32F2F (War/Axis)
    Blue: #1976D2 (Allies)
    Yellow: #FBC02D (Highlight)
    Dark: #212121 (Text/BG)
    Light: #FAFAFA (Cards)
    -->
    <!-- 
    CONFIRMATION: 
    - Source Material Analyzed: "Resumen_SGM_Estilo_Barrio.md"
    - Narrative Plan: Intro -> Factions (Pie) -> Casualties (Bar) -> Timeline (HTML) -> Economy (Line) -> Aftermath.
    - NO SVG USED.
    - NO MERMAID JS USED.
    - Chart.js Tooltips configured for multiline.
    - Labels split at 16 chars.
    -->
</head>
<body class="bg-gray-100 text-gray-800 font-sans leading-relaxed">

    <!-- Navigation / Header -->
    <header class="bg-gray-900 text-white sticky top-0 z-50 shadow-lg border-b-4 border-yellow-500">
        <div class="container mx-auto px-4 py-4 flex justify-between items-center">
            <h1 class="text-xl md:text-2xl font-bold uppercase tracking-wider">SGM: El Resumen</h1>
            <nav class="hidden md:block">
                <ul class="flex space-x-6 text-sm font-semibold">
                    <li><a href="#intro" class="hover:text-yellow-400 transition">El Tiro</a></li>
                    <li><a href="#stats" class="hover:text-yellow-400 transition">Los Números</a></li>
                    <li><a href="#timeline" class="hover:text-yellow-400 transition">El Desmadre</a></li>
                    <li><a href="#economy" class="hover:text-yellow-400 transition">La Lana</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="container mx-auto px-4 py-8 space-y-12">

        <!-- SECTION 1: INTRO -->
        <section id="intro" class="text-center max-w-4xl mx-auto mb-12">
            <h2 class="text-4xl md:text-6xl font-extrabold text-red-700 mb-4">El Gran Desmadre Global</h2>
            <p class="text-xl md:text-2xl text-gray-600 font-medium italic mb-6">"Imagínate que el mundo era una vecindad en los años 30 y todos andaban bien calientes."</p>
            <div class="bg-white p-6 rounded-lg shadow-md border-l-8 border-red-600 text-left">
                <p class="text-lg">
                    La <strong>Segunda Guerra Mundial (1939-1945)</strong> no fue un pleito de cantina cualquiera. Fue la bronca más grande de la historia. Se murieron entre <strong>70 y 85 millones de personas</strong>. Aquí te explicamos cómo estuvo el *business* económico y político, estilo barrio pero con datos duros.
                </p>
            </div>
        </section>

        <!-- SECTION 2: THE TEAMS (PIE CHART) -->
        <section class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
            <div class="order-2 md:order-1">
                <div class="bg-white rounded-xl shadow-lg p-6 hover-card border-t-4 border-blue-600">
                    <h3 class="text-2xl font-bold mb-4 text-gray-800">¿Quién contra Quién?</h3>
                    <p class="mb-4 text-gray-600">
                        El mundo se partió en dos bandos, como en una final de fut pero con tanques. Por un lado, los tóxicos que querían todo el pastel, y por el otro, los que cayeron al quite para pararlos.
                    </p>
                    <div class="chart-container">
                        <canvas id="factionsChart"></canvas>
                    </div>
                    <p class="mt-4 text-sm text-gray-500 text-center">
                        <em>El Eje (Alemania, Japón, Italia) vs. Los Aliados (UK, Francia, URSS, USA).</em>
                    </p>
                </div>
            </div>
            <div class="order-1 md:order-2 space-y-4">
                <h3 class="text-3xl font-bold text-gray-900 border-b-4 border-yellow-500 inline-block pb-1">Los Bandos</h3>
                <div class="bg-red-50 p-4 rounded-lg border-l-4 border-red-600">
                    <h4 class="font-bold text-red-700 text-xl">👹 EL EJE (Los Malos)</h4>
                    <p><strong>Alemania:</strong> El líder tóxico con rencor.</p>
                    <p><strong>Japón:</strong> El intenso que quería Asia.</p>
                    <p><strong>Italia:</strong> El que nada más estorbaba.</p>
                </div>
                <div class="bg-blue-50 p-4 rounded-lg border-l-4 border-blue-600">
                    <h4 class="font-bold text-blue-700 text-xl">🛡️ LOS ALIADOS (El Quite)</h4>
                    <p><strong>Gran Bretaña:</strong> Aguantaron vara solos.</p>
                    <p><strong>URSS (Rusia):</strong> Pusieron los muertos.</p>
                    <p><strong>USA (Gringos):</strong> Llegaron tarde pero con varo.</p>
                </div>
            </div>
        </section>

        <!-- SECTION 3: THE COST (BAR CHART) -->
        <section id="stats" class="bg-gray-900 text-white rounded-3xl p-8 shadow-2xl">
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <div class="lg:col-span-1 flex flex-col justify-center">
                    <h3 class="text-yellow-400 font-bold tracking-widest uppercase mb-2">Costo Humano</h3>
                    <h2 class="text-5xl font-extrabold mb-4">85 Millones<span class="text-red-500">.</span></h2>
                    <p class="text-gray-300 text-lg mb-6">
                        Es difícil imaginar a tanta gente. Para que te des una idea, la URSS perdió tanta raza que afectó su demografía por décadas. Alemania y Polonia quedaron en ruinas.
                    </p>
                    <div class="bg-gray-800 p-4 rounded border border-gray-700">
                        <span class="text-3xl mr-2">☠️</span>
                        <span class="font-bold">El Holocausto:</span>
                        <p class="text-sm mt-1 text-gray-400">
                            Los nazis armaron fábricas de muerte. 6 Millones de judíos asesinados sistemáticamente. La parte más oscura de la historia.
                        </p>
                    </div>
                </div>
                <div class="lg:col-span-2">
                    <div class="chart-container bg-white rounded-lg p-2">
                        <canvas id="casualtiesChart"></canvas>
                    </div>
                    <p class="text-center text-sm text-gray-400 mt-2">Muertes estimadas (Militares y Civiles) por país principal.</p>
                </div>
            </div>
        </section>

        <!-- SECTION 4: TIMELINE (HTML/CSS) -->
        <section id="timeline">
            <div class="text-center mb-10">
                <h2 class="text-3xl md:text-4xl font-bold text-gray-800">Cronología del Desmadre</h2>
                <p class="text-gray-600 mt-2">Del "Este terreno es mío" hasta el "Game Over".</p>
            </div>
            
            <div class="relative wrap overflow-hidden p-4 h-full">
                <!-- Vertical Line -->
                <div class="border-2-2 absolute border-opacity-20 border-gray-700 h-full border" style="left: 50%"></div>
                
                <!-- 1939 Event -->
                <div class="mb-8 flex justify-between items-center w-full right-timeline">
                    <div class="order-1 w-5/12"></div>
                    <div class="z-20 flex items-center order-1 bg-red-600 shadow-xl w-8 h-8 rounded-full">
                        <h1 class="mx-auto font-semibold text-lg text-white">1</h1>
                    </div>
                    <div class="order-1 bg-white rounded-lg shadow-xl w-5/12 px-6 py-4 border-t-4 border-red-500">
                        <h3 class="mb-1 font-bold text-gray-800 text-xl">1939: El Detonante</h3>
                        <p class="text-sm leading-snug tracking-wide text-gray-600 text-opacity-100">
                            Hitler invade Polonia. Francia e Inglaterra le dicen "bájale de huevos" y declaran la guerra. Empieza la <strong>Blitzkrieg</strong> (Guerra Relámpago).
                        </p>
                    </div>
                </div>

                <!-- 1941 Event -->
                <div class="mb-8 flex justify-between flex-row-reverse items-center w-full left-timeline">
                    <div class="order-1 w-5/12"></div>
                    <div class="z-20 flex items-center order-1 bg-blue-600 shadow-xl w-8 h-8 rounded-full">
                        <h1 class="mx-auto font-semibold text-lg text-white">2</h1>
                    </div>
                    <div class="order-1 bg-white rounded-lg shadow-xl w-5/12 px-6 py-4 border-t-4 border-blue-500">
                        <h3 class="mb-1 font-bold text-gray-800 text-xl">1941: El Error y la Traición</h3>
                        <p class="text-sm leading-snug tracking-wide text-gray-600 text-opacity-100">
                            1. Hitler traiciona a Stalin e invade Rusia (Operación Barbarroja).<br>
                            2. Japón bombardea <strong>Pearl Harbor</strong>. Los gringos entran al chat con toda su industria.
                        </p>
                    </div>
                </div>

                <!-- 1942-43 Event -->
                <div class="mb-8 flex justify-between items-center w-full right-timeline">
                    <div class="order-1 w-5/12"></div>
                    <div class="z-20 flex items-center order-1 bg-yellow-500 shadow-xl w-8 h-8 rounded-full">
                        <h1 class="mx-auto font-semibold text-lg text-white">3</h1>
                    </div>
                    <div class="order-1 bg-white rounded-lg shadow-xl w-5/12 px-6 py-4 border-t-4 border-yellow-500">
                        <h3 class="mb-1 font-bold text-gray-800 text-xl">1942-1943: Stalingrado</h3>
                        <p class="text-sm leading-snug tracking-wide text-gray-600 text-opacity-100">
                            El punto de quiebre. Los nazis se congelan en Rusia. Ley de Pareto: Esta batalla definió gran parte del resultado.
                        </p>
                    </div>
                </div>

                <!-- 1945 Event -->
                <div class="mb-8 flex justify-between flex-row-reverse items-center w-full left-timeline">
                    <div class="order-1 w-5/12"></div>
                    <div class="z-20 flex items-center order-1 bg-gray-800 shadow-xl w-8 h-8 rounded-full">
                        <h1 class="mx-auto font-semibold text-lg text-white">4</h1>
                    </div>
                    <div class="order-1 bg-white rounded-lg shadow-xl w-5/12 px-6 py-4 border-t-4 border-gray-800">
                        <h3 class="mb-1 font-bold text-gray-800 text-xl">1945: Game Over</h3>
                        <p class="text-sm leading-snug tracking-wide text-gray-600 text-opacity-100">
                            Hitler se suicida en su búnker. USA tira dos bombas atómicas en Japón (Hiroshima y Nagasaki). Fin del juego.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION 5: ECONOMICS (LINE CHART) -->
        <section id="economy" class="bg-white rounded-xl shadow-lg p-8 border-t-8 border-green-600">
            <div class="mb-6">
                <h2 class="text-3xl font-bold text-gray-800">Economía de Guerra Total</h2>
                <p class="text-gray-600">
                    Aquí es donde entra tu carrera, Percy. Para ganar, los países tuvieron que cambiar todo su modelo económico. El "Keynesianismo Militar" sacó al mundo de la Gran Depresión.
                </p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div>
                    <div class="chart-container">
                        <canvas id="economyChart"></canvas>
                    </div>
                    <p class="text-xs text-center text-gray-500 mt-2">
                        *Representación conceptual del cambio en la producción industrial (USA/Aliados).
                    </p>
                </div>
                <div class="flex flex-col justify-center space-y-4">
                    <div class="flex items-start">
                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-green-100 flex items-center justify-center text-2xl">👷‍♀️</div>
                        <div class="ml-4">
                            <h4 class="text-lg font-bold text-gray-900">Mujeres al Jale</h4>
                            <p class="text-gray-600 text-sm">Los hombres peleaban, así que las mujeres tomaron las fábricas. La fuerza laboral cambió para siempre.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-red-100 flex items-center justify-center text-2xl">🏭</div>
                        <div class="ml-4">
                            <h4 class="text-lg font-bold text-gray-900">Guerra Total</h4>
                            <p class="text-gray-600 text-sm">Dejaron de hacer coches para hacer tanques. Toda la economía enfocada en destruir al enemigo.</p>
                        </div>
                    </div>
                    <div class="flex items-start">
                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-blue-100 flex items-center justify-center text-2xl">💰</div>
                        <div class="ml-4">
                            <h4 class="text-lg font-bold text-gray-900">Plan Marshall</h4>
                            <p class="text-gray-600 text-sm">Después de la guerra, Europa estaba rota. USA prestó lana para reconstruir (y ganar aliados contra los rojos).</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- SECTION 6: CONCLUSION -->
        <section class="bg-gray-800 text-white p-8 rounded-lg text-center">
            <h2 class="text-3xl font-bold mb-6 text-yellow-400">¿Cómo quedó la cosa?</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 border border-gray-600 rounded bg-gray-700">
                    <h3 class="text-xl font-bold mb-2">🇺🇸 USA (Capitalismo)</h3>
                    <p class="text-sm">Quedaron como los nuevos jefes del barrio con mucho varo.</p>
                </div>
                <div class="p-4 border border-gray-600 rounded bg-gray-700">
                    <h3 class="text-xl font-bold mb-2">☭ URSS (Comunismo)</h3>
                    <p class="text-sm">Quedaron poderosos pero heridos. No se querían con los gringos.</p>
                </div>
            </div>
            <p class="mt-6 text-xl font-light">
                Esto dio inicio a la <strong>Guerra Fría</strong>. Se creó la <strong>ONU</strong> para evitar otro desmadre igual (aunque a veces no les sale).
            </p>
        </section>

    </main>

    <footer class="bg-gray-900 text-gray-400 py-6 text-center text-sm">
        <p>Generado para Percy (Facultad de Economía, UNAM) | Estilo Barrio Educativo</p>
    </footer>

    <script>
        // --- HELPER FUNCTION FOR LABEL WRAPPING (16 CHAR LIMIT) ---
        function splitLabel(label) {
            if (label.length <= 16) return label;
            const words = label.split(' ');
            const lines = [];
            let currentLine = words[0];

            for (let i = 1; i < words.length; i++) {
                if ((currentLine + " " + words[i]).length <= 16) {
                    currentLine += " " + words[i];
                } else {
                    lines.push(currentLine);
                    currentLine = words[i];
                }
            }
            lines.push(currentLine);
            return lines;
        }

        // --- COMMON TOOLTIP CONFIGURATION ---
        const commonTooltipPlugin = {
            tooltip: {
                callbacks: {
                    title: function(tooltipItems) {
                        const item = tooltipItems[0];
                        let label = item.chart.data.labels[item.dataIndex];
                        if (Array.isArray(label)) {
                            return label.join(' ');
                        } else {
                            return label;
                        }
                    }
                }
            }
        };

        // --- CHART 1: FACTIONS (DOUGHNUT) ---
        const ctxFactions = document.getElementById('factionsChart').getContext('2d');
        const labelsFactions = ["Los Aliados (USA, UK, URSS)", "El Eje (Alemania, Japón, Italia)"];
        const processedLabelsFactions = labelsFactions.map(splitLabel);

        new Chart(ctxFactions, {
            type: 'doughnut',
            data: {
                labels: processedLabelsFactions,
                datasets: [{
                    data: [65, 35], // Conceptual strength/size
                    backgroundColor: ['#1976D2', '#D32F2F'], // Blue vs Red
                    borderWidth: 2,
                    borderColor: '#ffffff'
                }]
            },
            options: {
                maintainAspectRatio: false,
                responsive: true,
                plugins: {
                    ...commonTooltipPlugin,
                    legend: {
                        position: 'bottom',
                        labels: { font: { size: 14 } }
                    }
                }
            }
        });

        // --- CHART 2: CASUALTIES (BAR) ---
        // Data approximation for visualization (in Millions)
        const ctxCasualties = document.getElementById('casualtiesChart').getContext('2d');
        const labelsCasualties = ["URSS (Rusia)", "China", "Alemania", "Polonia", "Japón", "USA"];
        const processedLabelsCasualties = labelsCasualties.map(splitLabel);

        new Chart(ctxCasualties, {
            type: 'bar',
            data: {
                labels: processedLabelsCasualties,
                datasets: [{
                    label: 'Muertes Estimadas (Millones)',
                    data: [26, 20, 7, 6, 3, 0.4],
                    backgroundColor: [
                        '#B71C1C', // URSS (Dark Red)
                        '#EF5350', // China
                        '#212121', // Germany (Black/Dark)
                        '#757575', // Poland
                        '#D32F2F', // Japan
                        '#1976D2'  // USA (Blue)
                    ],
                    borderRadius: 4
                }]
            },
            options: {
                maintainAspectRatio: false,
                responsive: true,
                indexAxis: 'y', // Horizontal bar for better label reading
                scales: {
                    x: {
                        beginAtZero: true,
                        grid: { color: '#e0e0e0' },
                        ticks: { color: '#000' }
                    },
                    y: {
                        ticks: { color: '#000', font: {weight: 'bold'} }
                    }
                },
                plugins: {
                    ...commonTooltipPlugin,
                    legend: { display: false }
                }
            }
        });

        // --- CHART 3: ECONOMY (LINE) ---
        // Conceptual chart showing the shift to War Production
        const ctxEconomy = document.getElementById('economyChart').getContext('2d');
        const labelsEconomy = ["1938", "1939 (Inicio)", "1941 (USA Entra)", "1943 (Pico)", "1945 (Fin)"];
        const processedLabelsEconomy = labelsEconomy.map(splitLabel);

        new Chart(ctxEconomy, {
            type: 'line',
            data: {
                labels: processedLabelsEconomy,
                datasets: [
                    {
                        label: 'Producción Militar',
                        data: [10, 30, 60, 95, 40],
                        borderColor: '#D32F2F',
                        backgroundColor: 'rgba(211, 47, 47, 0.1)',
                        fill: true,
                        tension: 0.4,
                        borderWidth: 3
                    },
                    {
                        label: 'Bienes de Consumo Civil',
                        data: [90, 70, 40, 5, 60],
                        borderColor: '#1976D2',
                        borderDash: [5, 5],
                        tension: 0.4,
                        borderWidth: 2
                    }
                ]
            },
            options: {
                maintainAspectRatio: false,
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true,
                        title: { display: true, text: '% de la Economía' }
                    }
                },
                plugins: {
                    ...commonTooltipPlugin,
                    legend: { position: 'top' }
                }
            }
        });

    </script>
</body>
</html>
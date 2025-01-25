vector<string> separar_string(string frase){
    stringstream ss(frase);
    string palavra;
    vector<string> palavras;

    while (ss >> palavra){
        palavras.push_back(palavra);
    }

    return palavras;
}

vector<int> separar_int(string frase){
    stringstream ss(frase);
    string numero;
    vector<int> numeros;

    while (ss >> numero){
        numeros.push_back(stoi(numero));
    }

    return numeros;
}
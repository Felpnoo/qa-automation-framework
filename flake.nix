{
  description = "Python QA Automation Environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          (python3.withPackages (ps: with ps; [
            playwright
            pytest
            pytest-playwright
            pytest-html
          ]))
          playwright-driver.browsers
        ];

        shellHook = ''
          echo "🧪 Ambiente de QA Carregado!"
          export PLAYWRIGHT_BROWSERS_PATH=${pkgs.playwright-driver.browsers}
        '';
      };
    };
}

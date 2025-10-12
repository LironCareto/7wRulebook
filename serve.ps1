<#
Serve the site locally. Preference order:
 1) bundle exec jekyll serve
 2) jekyll serve (if installed as gem)
 3) Docker jekyll image

Run from the repository root in PowerShell:
  .\serve.ps1
#>

Push-Location $PSScriptRoot
try {
    if (Get-Command bundle -ErrorAction SilentlyContinue) {
        Write-Host "Running: bundle exec jekyll serve --livereload --incremental"
        & bundle exec jekyll serve --livereload --incremental
        return
    }

    if (Get-Command jekyll -ErrorAction SilentlyContinue) {
        Write-Host "Running: jekyll serve --livereload --incremental"
        & jekyll serve --livereload --incremental
        return
    }

    if (Get-Command docker -ErrorAction SilentlyContinue) {
        Write-Host "Bundle not found; using Docker image jekyll/jekyll:4"
        $pwdEscaped = ${PWD}.Path -replace '\\','/'
        docker run --rm -it -p 4000:4000 -v "${pwdEscaped}:/srv/jekyll" jekyll/jekyll:4 jekyll serve --watch --incremental --livereload --host 0.0.0.0
        return
    }

    Write-Error "Neither 'bundle', 'jekyll' nor 'docker' were found in PATH. Install Ruby + Bundler or Docker Desktop."
}
finally {
    Pop-Location
}

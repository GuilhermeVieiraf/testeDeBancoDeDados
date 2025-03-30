-- 10 operadoras com maiores despesas no último trimestre
SELECT
    reg_ans,
    SUM(vl_saldo_final) AS total_despesas
FROM
    demonstracoes_contabeis
WHERE
    cd_conta_contabil = '411111'
    AND dt_competencia >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)
GROUP BY
    reg_ans
ORDER BY
    total_despesas DESC
LIMIT 10;

-- 10 operadoras com maiores despesas no último ano
SELECT
    reg_ans,
    SUM(vl_saldo_final) AS total_despesas
FROM
    demonstracoes_contabeis
WHERE
    cd_conta_contabil = '411111'
    AND dt_competencia >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY
    reg_ans
ORDER BY
    total_despesas DESC
LIMIT 10;
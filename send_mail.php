<?php
header('Content-Type: application/json; charset=utf-8');

// Honeypot anti-spam: se il campo nascosto "website" è compilato è un bot
if (!empty($_POST['website'])) {
    echo json_encode(['success' => true]);
    exit;
}

$to = 'info@studiotarantovancheri.it';

$name    = htmlspecialchars(strip_tags(trim($_POST['name']    ?? '')));
$email   = filter_var(trim($_POST['email']   ?? ''), FILTER_SANITIZE_EMAIL);
$subject = htmlspecialchars(strip_tags(trim($_POST['subject'] ?? '')));
$message = htmlspecialchars(strip_tags(trim($_POST['message'] ?? '')));

// Validazione campi obbligatori
if (!$name || !$email || !$subject || !$message) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Tutti i campi sono obbligatori.']);
    exit;
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Indirizzo email non valido.']);
    exit;
}

$email_subject = "Messaggio dal sito: $subject";

$email_body  = "Nuovo messaggio dal sito Studio Taranto-Vancheri\n";
$email_body .= str_repeat("-", 50) . "\n\n";
$email_body .= "Nome:    $name\n";
$email_body .= "Email:   $email\n";
$email_body .= "Oggetto: $subject\n\n";
$email_body .= "Messaggio:\n$message\n";

$headers  = "From: noreply@studiotarantovancheri.it\r\n";
$headers .= "Reply-To: $email\r\n";
$headers .= "X-Mailer: PHP/" . phpversion();

if (mail($to, $email_subject, $email_body, $headers)) {
    echo json_encode(['success' => true, 'message' => 'Messaggio inviato con successo! Ti risponderemo al più presto.']);
} else {
    http_response_code(500);
    echo json_encode(['success' => false, 'message' => "Errore nell'invio. Riprova più tardi o contattaci telefonicamente."]);
}
